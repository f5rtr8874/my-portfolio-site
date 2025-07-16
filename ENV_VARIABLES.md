# Environment Variables for Production

## 📋 Required Environment Variables

### For Railway (Backend)
```
PORT=8001
MONGO_URL=mongodb://localhost:27017/portfolio_db
```

### For Vercel (Frontend)
```
VITE_BACKEND_URL=https://your-backend-url.railway.app
```

## 🔄 How to Set Environment Variables

### Railway
1. Go to your Railway project dashboard
2. Click on "Variables" tab
3. Add each variable:
   - Key: `PORT`, Value: `8001`
   - Key: `MONGO_URL`, Value: `mongodb://localhost:27017/portfolio_db`

### Vercel
1. Go to your Vercel project dashboard
2. Click on "Settings" → "Environment Variables"
3. Add the variable:
   - Key: `VITE_BACKEND_URL`
   - Value: `https://your-backend-url.railway.app` (replace with your actual Railway URL)

## 🗄️ Database Options

### Option 1: Local MongoDB (Simple)
Use the default local MongoDB connection:
```
MONGO_URL=mongodb://localhost:27017/portfolio_db
```

### Option 2: MongoDB Atlas (Recommended for Production)
1. Create a free MongoDB Atlas account
2. Create a cluster
3. Get your connection string
4. Update MONGO_URL:
```
MONGO_URL=mongodb+srv://username:password@cluster0.mongodb.net/portfolio_db
```

## 🔐 Security Note
- Never commit environment variables to your repository
- Use the platform's environment variable settings
- Keep your database credentials secure