import os
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
import uuid
import base64
from io import BytesIO

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
MONGO_URL = os.environ.get('MONGO_URL', 'mongodb://localhost:27017/portfolio_db')
client = MongoClient(MONGO_URL)
db = client.portfolio_db

# Pydantic models
class Project(BaseModel):
    id: str
    title: str
    description: str
    category: str  # photography, videography, 3d_design
    image: str  # base64 encoded image
    created_at: datetime
    featured: bool = False

class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    message: str
    created_at: datetime

class ContactRequest(BaseModel):
    name: str
    email: EmailStr
    message: str

# API Routes
@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "message": "Portfolio API is running"}

@app.get("/api/projects")
async def get_projects(category: Optional[str] = None):
    """Get all projects or filter by category"""
    query = {}
    if category:
        query["category"] = category
    
    projects = list(db.projects.find(query))
    for project in projects:
        project["_id"] = str(project["_id"])
    
    return {"projects": projects}

@app.get("/api/projects/{project_id}")
async def get_project(project_id: str):
    """Get a specific project by ID"""
    project = db.projects.find_one({"id": project_id})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    project["_id"] = str(project["_id"])
    return project

@app.post("/api/projects")
async def create_project(
    title: str = Form(...),
    description: str = Form(...),
    category: str = Form(...),
    featured: bool = Form(False),
    image: UploadFile = File(...)
):
    """Create a new project"""
    # Convert image to base64
    image_data = await image.read()
    image_base64 = base64.b64encode(image_data).decode('utf-8')
    
    project = {
        "id": str(uuid.uuid4()),
        "title": title,
        "description": description,
        "category": category,
        "image": image_base64,
        "featured": featured,
        "created_at": datetime.now()
    }
    
    result = db.projects.insert_one(project)
    project["_id"] = str(result.inserted_id)
    
    return {"message": "Project created successfully", "project": project}

@app.post("/api/contact")
async def submit_contact(contact: ContactRequest):
    """Submit a contact form message"""
    message = {
        "name": contact.name,
        "email": contact.email,
        "message": contact.message,
        "created_at": datetime.now()
    }
    
    result = db.contact_messages.insert_one(message)
    message["_id"] = str(result.inserted_id)
    
    return {"message": "Contact message submitted successfully", "id": str(result.inserted_id)}

@app.get("/api/contact")
async def get_contact_messages():
    """Get all contact messages (admin only)"""
    messages = list(db.contact_messages.find().sort("created_at", -1))
    for message in messages:
        message["_id"] = str(message["_id"])
    
    return {"messages": messages}

if __name__ == "__main__":
    import uvicorn
    # Use PORT environment variable for Railway deployment
    port = int(os.environ.get("PORT", 8001))
    uvicorn.run(app, host="0.0.0.0", port=port)