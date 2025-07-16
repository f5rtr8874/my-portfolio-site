#!/usr/bin/env python3
"""
Portfolio Website Backend API Testing Suite
Tests all backend endpoints for the portfolio website
"""

import requests
import json
import base64
import io
from datetime import datetime
import uuid

# Backend URL from environment
BACKEND_URL = "http://localhost:8001"

class PortfolioAPITester:
    def __init__(self):
        self.base_url = BACKEND_URL
        self.test_results = []
        self.created_project_id = None
        
    def log_test(self, test_name, success, message, response_data=None):
        """Log test results"""
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}: {message}")
        self.test_results.append({
            "test": test_name,
            "success": success,
            "message": message,
            "response_data": response_data
        })
    
    def create_test_image(self):
        """Create a simple test image in base64 format"""
        # Create a simple 1x1 pixel PNG image
        import struct
        
        # PNG header
        png_data = b'\x89PNG\r\n\x1a\n'
        
        # IHDR chunk (13 bytes data)
        ihdr_data = struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0)  # 1x1, 8-bit, RGB
        ihdr_crc = 0x37  # Simplified CRC for this specific data
        png_data += struct.pack('>I', 13) + b'IHDR' + ihdr_data + struct.pack('>I', ihdr_crc)
        
        # IDAT chunk (minimal data)
        idat_data = b'\x78\x9c\x62\x00\x00\x00\x02\x00\x01'
        idat_crc = 0x9ba60e2b  # CRC for this data
        png_data += struct.pack('>I', len(idat_data)) + b'IDAT' + idat_data + struct.pack('>I', idat_crc)
        
        # IEND chunk
        png_data += struct.pack('>I', 0) + b'IEND' + struct.pack('>I', 0xae426082)
        
        return png_data

    def test_health_check(self):
        """Test GET /api/health endpoint"""
        try:
            response = requests.get(f"{self.base_url}/api/health")
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "healthy":
                    self.log_test("Health Check", True, "API is healthy and responding")
                else:
                    self.log_test("Health Check", False, f"Unexpected response: {data}")
            else:
                self.log_test("Health Check", False, f"HTTP {response.status_code}: {response.text}")
        except Exception as e:
            self.log_test("Health Check", False, f"Connection error: {str(e)}")

    def test_get_all_projects(self):
        """Test GET /api/projects (all projects)"""
        try:
            response = requests.get(f"{self.base_url}/api/projects")
            if response.status_code == 200:
                data = response.json()
                if "projects" in data and isinstance(data["projects"], list):
                    self.log_test("Get All Projects", True, f"Retrieved {len(data['projects'])} projects")
                else:
                    self.log_test("Get All Projects", False, f"Invalid response format: {data}")
            else:
                self.log_test("Get All Projects", False, f"HTTP {response.status_code}: {response.text}")
        except Exception as e:
            self.log_test("Get All Projects", False, f"Connection error: {str(e)}")

    def test_get_projects_by_category(self):
        """Test GET /api/projects with category filters"""
        categories = ["photography", "videography", "3d_design"]
        
        for category in categories:
            try:
                response = requests.get(f"{self.base_url}/api/projects", params={"category": category})
                if response.status_code == 200:
                    data = response.json()
                    if "projects" in data and isinstance(data["projects"], list):
                        # Check if all returned projects have the correct category
                        valid_category = all(project.get("category") == category for project in data["projects"])
                        if valid_category:
                            self.log_test(f"Get Projects - {category}", True, 
                                        f"Retrieved {len(data['projects'])} {category} projects")
                        else:
                            self.log_test(f"Get Projects - {category}", False, 
                                        "Some projects have incorrect category")
                    else:
                        self.log_test(f"Get Projects - {category}", False, f"Invalid response format: {data}")
                else:
                    self.log_test(f"Get Projects - {category}", False, 
                                f"HTTP {response.status_code}: {response.text}")
            except Exception as e:
                self.log_test(f"Get Projects - {category}", False, f"Connection error: {str(e)}")

    def test_create_project(self):
        """Test POST /api/projects (create project with file upload)"""
        try:
            # Create test image
            test_image = self.create_test_image()
            
            # Prepare form data
            files = {
                'image': ('test_image.png', test_image, 'image/png')
            }
            
            data = {
                'title': 'Mountain Landscape Photography',
                'description': 'A stunning landscape photograph capturing the beauty of mountain ranges during golden hour.',
                'category': 'photography',
                'featured': True
            }
            
            response = requests.post(f"{self.base_url}/api/projects", files=files, data=data)
            
            if response.status_code == 200:
                result = response.json()
                if "project" in result and "id" in result["project"]:
                    self.created_project_id = result["project"]["id"]
                    self.log_test("Create Project", True, 
                                f"Project created successfully with ID: {self.created_project_id}")
                else:
                    self.log_test("Create Project", False, f"Invalid response format: {result}")
            else:
                self.log_test("Create Project", False, f"HTTP {response.status_code}: {response.text}")
        except Exception as e:
            self.log_test("Create Project", False, f"Error: {str(e)}")

    def test_get_specific_project(self):
        """Test GET /api/projects/{id} for specific project"""
        if not self.created_project_id:
            # Try to get any existing project first
            try:
                response = requests.get(f"{self.base_url}/api/projects")
                if response.status_code == 200:
                    data = response.json()
                    if data["projects"]:
                        self.created_project_id = data["projects"][0].get("id")
            except:
                pass
        
        if self.created_project_id:
            try:
                response = requests.get(f"{self.base_url}/api/projects/{self.created_project_id}")
                if response.status_code == 200:
                    project = response.json()
                    if "id" in project and project["id"] == self.created_project_id:
                        self.log_test("Get Specific Project", True, 
                                    f"Retrieved project: {project.get('title', 'Unknown')}")
                    else:
                        self.log_test("Get Specific Project", False, f"Invalid project data: {project}")
                else:
                    self.log_test("Get Specific Project", False, 
                                f"HTTP {response.status_code}: {response.text}")
            except Exception as e:
                self.log_test("Get Specific Project", False, f"Error: {str(e)}")
        else:
            # Test with non-existent ID
            fake_id = str(uuid.uuid4())
            try:
                response = requests.get(f"{self.base_url}/api/projects/{fake_id}")
                if response.status_code == 404:
                    self.log_test("Get Specific Project (404)", True, "Correctly returned 404 for non-existent project")
                else:
                    self.log_test("Get Specific Project (404)", False, 
                                f"Expected 404, got {response.status_code}")
            except Exception as e:
                self.log_test("Get Specific Project (404)", False, f"Error: {str(e)}")

    def test_contact_form_valid(self):
        """Test POST /api/contact with valid contact form data"""
        contact_data = {
            "name": "Sarah Johnson",
            "email": "sarah.johnson@email.com",
            "message": "Hi! I'm interested in hiring you for a wedding photography session. Could we discuss your packages and availability for next summer?"
        }
        
        try:
            response = requests.post(f"{self.base_url}/api/contact", 
                                   json=contact_data,
                                   headers={"Content-Type": "application/json"})
            
            if response.status_code == 200:
                result = response.json()
                if "message" in result and "id" in result:
                    self.log_test("Contact Form (Valid)", True, 
                                f"Contact message submitted successfully with ID: {result['id']}")
                else:
                    self.log_test("Contact Form (Valid)", False, f"Invalid response format: {result}")
            else:
                self.log_test("Contact Form (Valid)", False, 
                            f"HTTP {response.status_code}: {response.text}")
        except Exception as e:
            self.log_test("Contact Form (Valid)", False, f"Error: {str(e)}")

    def test_contact_form_invalid(self):
        """Test POST /api/contact with invalid data"""
        # Test missing fields
        invalid_data_sets = [
            {"name": "John", "email": "invalid-email", "message": "Test"},  # Invalid email
            {"name": "", "email": "test@email.com", "message": "Test"},     # Empty name
            {"name": "John", "email": "test@email.com", "message": ""},     # Empty message
            {"email": "test@email.com", "message": "Test"},                 # Missing name
            {"name": "John", "message": "Test"},                            # Missing email
            {"name": "John", "email": "test@email.com"}                     # Missing message
        ]
        
        for i, invalid_data in enumerate(invalid_data_sets):
            try:
                response = requests.post(f"{self.base_url}/api/contact", 
                                       json=invalid_data,
                                       headers={"Content-Type": "application/json"})
                
                if response.status_code in [400, 422]:  # Bad request or validation error
                    self.log_test(f"Contact Form Invalid #{i+1}", True, 
                                f"Correctly rejected invalid data: {response.status_code}")
                else:
                    self.log_test(f"Contact Form Invalid #{i+1}", False, 
                                f"Expected 400/422, got {response.status_code}")
            except Exception as e:
                self.log_test(f"Contact Form Invalid #{i+1}", False, f"Error: {str(e)}")

    def test_get_contact_messages(self):
        """Test GET /api/contact to retrieve contact messages"""
        try:
            response = requests.get(f"{self.base_url}/api/contact")
            if response.status_code == 200:
                data = response.json()
                if "messages" in data and isinstance(data["messages"], list):
                    self.log_test("Get Contact Messages", True, 
                                f"Retrieved {len(data['messages'])} contact messages")
                else:
                    self.log_test("Get Contact Messages", False, f"Invalid response format: {data}")
            else:
                self.log_test("Get Contact Messages", False, 
                            f"HTTP {response.status_code}: {response.text}")
        except Exception as e:
            self.log_test("Get Contact Messages", False, f"Error: {str(e)}")

    def run_all_tests(self):
        """Run all backend API tests"""
        print("=" * 60)
        print("PORTFOLIO WEBSITE BACKEND API TESTING")
        print("=" * 60)
        
        # Test in logical order
        self.test_health_check()
        print()
        
        print("PROJECTS API TESTS:")
        print("-" * 30)
        self.test_get_all_projects()
        self.test_get_projects_by_category()
        self.test_create_project()
        self.test_get_specific_project()
        print()
        
        print("CONTACT API TESTS:")
        print("-" * 30)
        self.test_contact_form_valid()
        self.test_contact_form_invalid()
        self.test_get_contact_messages()
        print()
        
        # Summary
        print("=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for result in self.test_results if result["success"])
        total = len(self.test_results)
        
        print(f"Total Tests: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {total - passed}")
        print(f"Success Rate: {(passed/total)*100:.1f}%")
        
        if total - passed > 0:
            print("\nFAILED TESTS:")
            for result in self.test_results:
                if not result["success"]:
                    print(f"  ❌ {result['test']}: {result['message']}")
        
        return passed == total

if __name__ == "__main__":
    tester = PortfolioAPITester()
    success = tester.run_all_tests()
    
    if success:
        print("\n🎉 All tests passed! Backend API is working correctly.")
    else:
        print("\n⚠️  Some tests failed. Check the details above.")