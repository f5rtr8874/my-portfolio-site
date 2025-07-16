# Portfolio Website

A personal portfolio website showcasing photography, videography, and 3D design work.

## 🌟 Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Project Showcase**: Display your work with category filtering
- **Contact Form**: Integrated contact form with backend validation
- **Professional Layout**: Clean, modern design with Tailwind CSS
- **Image Upload**: Support for project image uploads (base64 encoded)
- **Category Filtering**: Filter projects by Photography, Videography, or 3D Design

## 🚀 Live Demo

- **Frontend**: [Deploy to Vercel](https://vercel.com)
- **Backend**: [Deploy to Railway](https://railway.app)

## 🛠️ Tech Stack

### Frontend
- **React 18** - Modern React with hooks
- **Vite** - Fast build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **React Router** - Client-side routing
- **Axios** - HTTP client for API calls
- **Lucide React** - Beautiful icons

### Backend
- **FastAPI** - Modern Python web framework
- **MongoDB** - NoSQL database
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **Python Multipart** - File upload support

## 📦 Installation

### Prerequisites
- Node.js 16+ and yarn
- Python 3.8+
- MongoDB (local or Atlas)

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd portfolio-website
   ```

2. **Backend Setup**
   ```bash
   cd backend
   pip install -r requirements.txt
   cp .env.example .env  # Configure your environment variables
   python server.py
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   yarn install
   cp .env.example .env  # Configure your environment variables
   yarn dev
   ```

## 🌐 Deployment

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed deployment instructions.

### Quick Deploy
1. **Backend**: Deploy to Railway
2. **Frontend**: Deploy to Vercel
3. **Database**: Use MongoDB Atlas (optional)

## 📂 Project Structure

```
portfolio-website/
├── backend/                 # FastAPI backend
│   ├── server.py           # Main application
│   ├── requirements.txt    # Python dependencies
│   └── .env               # Environment variables
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── utils/         # API utilities
│   │   └── main.jsx       # Entry point
│   ├── package.json       # Node dependencies
│   └── .env              # Environment variables
├── vercel.json            # Vercel configuration
├── railway.json           # Railway configuration
└── README.md             # This file
```

## 🎨 Customization

### Adding New Projects
1. Use the admin interface or API to add projects
2. Upload images (converted to base64)
3. Categorize as photography, videography, or 3d_design

### Styling
- Edit Tailwind CSS classes in components
- Customize colors in `tailwind.config.js`
- Add custom CSS in `src/index.css`

### Content
- Update about section in `src/components/About.jsx`
- Modify contact information in `src/components/Contact.jsx`
- Change hero content in `src/components/Hero.jsx`

## 📡 API Endpoints

### Projects
- `GET /api/projects` - Get all projects
- `GET /api/projects?category=photography` - Filter by category
- `GET /api/projects/{id}` - Get specific project
- `POST /api/projects` - Create new project

### Contact
- `POST /api/contact` - Submit contact form
- `GET /api/contact` - Get all messages (admin)

### Health
- `GET /api/health` - Health check

## 🔧 Environment Variables

See [ENV_VARIABLES.md](ENV_VARIABLES.md) for detailed environment variable configuration.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you need help with deployment or customization, please check:
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- [ENV_VARIABLES.md](ENV_VARIABLES.md)
- Create an issue in the repository

---

Built with ❤️ using React, FastAPI, and MongoDB
