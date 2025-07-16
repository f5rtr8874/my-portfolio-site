# 📋 Pre-Deployment Checklist

Before deploying your portfolio website, make sure you complete these steps:

## ✅ Preparation Steps

### 1. Create GitHub Repository
- [ ] Create a new repository on GitHub
- [ ] Push your code to the repository
- [ ] Make sure all files are committed

### 2. Sign Up for Deployment Services
- [ ] Sign up for [Railway](https://railway.app) (for backend)
- [ ] Sign up for [Vercel](https://vercel.com) (for frontend)
- [ ] Use your GitHub account for both services

### 3. Database Setup (Optional but Recommended)
- [ ] Sign up for [MongoDB Atlas](https://mongodb.com/cloud/atlas)
- [ ] Create a free cluster
- [ ] Get your connection string
- [ ] Whitelist all IP addresses (0.0.0.0/0) for development

## 🚀 Deployment Order

### Step 1: Deploy Backend First
1. **Railway Deployment**
   - [ ] Connect your GitHub repository
   - [ ] Railway auto-detects Python app
   - [ ] Set environment variables:
     ```
     PORT=8001
     MONGO_URL=mongodb://localhost:27017/portfolio_db
     ```
   - [ ] Wait for deployment to complete
   - [ ] **IMPORTANT**: Copy your Railway URL (e.g., https://your-app.railway.app)

### Step 2: Deploy Frontend
1. **Vercel Deployment**
   - [ ] Connect your GitHub repository
   - [ ] Set Root Directory to `frontend`
   - [ ] Set Build Command to `yarn build`
   - [ ] Set Output Directory to `dist`
   - [ ] Set environment variable:
     ```
     VITE_BACKEND_URL=https://your-railway-url.railway.app
     ```
   - [ ] Deploy and test

## 🔧 Environment Variables Reference

### Railway (Backend)
```
PORT=8001
MONGO_URL=mongodb://localhost:27017/portfolio_db
```

### Vercel (Frontend)
```
VITE_BACKEND_URL=https://your-backend-url.railway.app
```

## 🧪 Testing Your Deployment

After deployment, test these features:
- [ ] Homepage loads correctly
- [ ] Navigation works
- [ ] Projects section displays (even if empty)
- [ ] Contact form submits successfully
- [ ] Backend API health check returns 200

## 🆘 Troubleshooting

### Common Issues:
1. **Backend not starting**: Check Railway logs for Python errors
2. **Frontend shows API errors**: Verify VITE_BACKEND_URL is correct
3. **Database connection fails**: Check MongoDB connection string
4. **Build fails**: Ensure all dependencies are in requirements.txt/package.json

### Where to Find Logs:
- **Railway**: Project Dashboard → Deployments → View Logs
- **Vercel**: Project Dashboard → Functions → View Logs

## 📱 Post-Deployment

After successful deployment:
- [ ] Test all functionality
- [ ] Update portfolio content
- [ ] Add your projects via the API
- [ ] Share your live website URL!

---

Your portfolio website is ready for the world! 🌍✨