import React, { useState, useEffect } from 'react';
import { apiService } from '../utils/api';

const Projects = () => {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedCategory, setSelectedCategory] = useState('all');

  const categories = [
    { id: 'all', name: 'All Projects' },
    { id: 'photography', name: 'Photography' },
    { id: 'videography', name: 'Videography' },
    { id: '3d_design', name: '3D Design' },
  ];

  // Mock projects data for demonstration
  const mockProjects = [
    {
      id: '1',
      title: 'Urban Photography Series',
      description: 'A collection of urban landscape photographs capturing the essence of city life.',
      category: 'photography',
      image: 'https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=800&q=80',
      featured: true,
      created_at: new Date().toISOString()
    },
    {
      id: '2',
      title: 'Corporate Video Production',
      description: 'Professional corporate video showcasing company culture and values.',
      category: 'videography',
      image: 'https://images.unsplash.com/photo-1492619392975-8b37776069ab?w=800&q=80',
      featured: false,
      created_at: new Date().toISOString()
    },
    {
      id: '3',
      title: '3D Product Visualization',
      description: 'Detailed 3D renders for product marketing and visualization.',
      category: '3d_design',
      image: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&q=80',
      featured: true,
      created_at: new Date().toISOString()
    },
    {
      id: '4',
      title: 'Portrait Photography',
      description: 'Professional portrait sessions with creative lighting and composition.',
      category: 'photography',
      image: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&q=80',
      featured: false,
      created_at: new Date().toISOString()
    },
    {
      id: '5',
      title: 'Brand Video Campaign',
      description: 'Creative video campaign for brand awareness and engagement.',
      category: 'videography',
      image: 'https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?w=800&q=80',
      featured: false,
      created_at: new Date().toISOString()
    },
    {
      id: '6',
      title: 'Architectural 3D Render',
      description: 'Photorealistic 3D architectural visualization for construction projects.',
      category: '3d_design',
      image: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&q=80',
      featured: true,
      created_at: new Date().toISOString()
    }
  ];

  useEffect(() => {
    fetchProjects();
  }, [selectedCategory]);

  const fetchProjects = async () => {
    try {
      setLoading(true);
      // Try to fetch from API first
      const response = await apiService.getProjects(selectedCategory === 'all' ? null : selectedCategory);
      setProjects(response.data.projects || []);
      
      // If no projects from API, use mock data
      if (!response.data.projects || response.data.projects.length === 0) {
        const filteredMockProjects = selectedCategory === 'all' 
          ? mockProjects 
          : mockProjects.filter(project => project.category === selectedCategory);
        setProjects(filteredMockProjects);
      }
    } catch (err) {
      console.error('Error fetching projects:', err);
      // Fallback to mock data
      const filteredMockProjects = selectedCategory === 'all' 
        ? mockProjects 
        : mockProjects.filter(project => project.category === selectedCategory);
      setProjects(filteredMockProjects);
    } finally {
      setLoading(false);
    }
  };

  const handleCategoryFilter = (category) => {
    setSelectedCategory(category);
  };

  if (loading) {
    return (
      <section id="projects" className="section-padding">
        <div className="container-max">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600 mx-auto"></div>
            <p className="mt-4 text-gray-600">Loading projects...</p>
          </div>
        </div>
      </section>
    );
  }

  return (
    <section id="projects" className="section-padding">
      <div className="container-max">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-primary-900 mb-6">
            My Projects
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto mb-8">
            Explore my creative work across photography, videography, and 3D design
          </p>

          {/* Category Filter */}
          <div className="flex flex-wrap justify-center gap-4 mb-8">
            {categories.map((category) => (
              <button
                key={category.id}
                onClick={() => handleCategoryFilter(category.id)}
                className={`px-6 py-2 rounded-full transition-colors ${
                  selectedCategory === category.id
                    ? 'bg-primary-600 text-white'
                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                }`}
              >
                {category.name}
              </button>
            ))}
          </div>
        </div>

        {/* Projects Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {projects.map((project) => (
            <div key={project.id} className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
              <div className="h-48 bg-gray-200 overflow-hidden">
                <img
                  src={project.image.startsWith('data:') ? project.image : project.image}
                  alt={project.title}
                  className="w-full h-full object-cover hover:scale-105 transition-transform duration-300"
                />
              </div>
              <div className="p-6">
                <div className="flex items-center gap-2 mb-2">
                  <span className="text-sm text-primary-600 font-medium capitalize">
                    {project.category.replace('_', ' ')}
                  </span>
                  {project.featured && (
                    <span className="bg-yellow-100 text-yellow-800 text-xs px-2 py-1 rounded-full">
                      Featured
                    </span>
                  )}
                </div>
                <h3 className="text-xl font-semibold text-primary-900 mb-3">
                  {project.title}
                </h3>
                <p className="text-gray-600 mb-4">
                  {project.description}
                </p>
                <button className="text-primary-600 hover:text-primary-700 font-medium">
                  View Details →
                </button>
              </div>
            </div>
          ))}
        </div>

        {projects.length === 0 && !loading && (
          <div className="text-center py-16">
            <p className="text-gray-600 text-lg">No projects found for this category.</p>
          </div>
        )}
      </div>
    </section>
  );
};

export default Projects;