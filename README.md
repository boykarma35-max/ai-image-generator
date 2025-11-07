# AI Image Generator Website

Complete AI Image Generator Website with support for **Sora**, **Veo**, **DALL-E**, **Midjourney**, and **Stable Diffusion**.

Built with **Flask** (Python backend), **modern CSS** UI, and **SQL database** for user management and image history.

## Features

✨ **Multi-Model Support**
- Sora - OpenAI's video generation model
- Veo - Google's advanced video/image generation
- DALL-E - OpenAI's image generation
- Midjourney - Advanced AI art generation
- Stable Diffusion - Open-source image generation

🔐 **User Authentication**
- User registration and login
- Secure password hashing with bcrypt
- Session management with Flask-Login

🗂️ **Image Management**
- Save generated images to database
- Track image history per user
- View generation metadata (model, dimensions, time)

⚙️ **API Key Management**
- Store and manage API keys securely
- Support for multiple keys per model
- Easy key rotation

💾 **Database**
- SQLite/PostgreSQL support
- User profiles and history tracking
- Generation logs and metadata

## Project Structure

```
ai-image-generator/
├── backend/
│   ├── __init__.py
│   ├── config.py              # Configuration settings
│   ├── models.py              # Database models
│   ├── auth.py                # Authentication routes
│   ├── api.py                 # Image generation API
│   └── utils.py               # Helper functions
├── templates/
│   ├── index.html             # Main generator page
│   ├── login.html             # Login page
│   ├── register.html          # Registration page
│   └── profile.html           # User profile
├── static/
│   ├── css/
│   │   └── style.css          # Main stylesheet
│   └── js/
│       └── main.js            # Frontend logic
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- SQLite or PostgreSQL

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/boykarma35-max/ai-image-generator.git
   cd ai-image-generator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file**
   ```bash
   cp .env.example .env
   ```
   Update with your configuration:
   ```
   SECRET_KEY=your-secret-key
   DATABASE_URL=sqlite:///database.db
   SORA_API_KEY=your-sora-key
   VEO_API_KEY=your-veo-key
   DALL_E_API_KEY=your-dalle-key
   MIDJOURNEY_API_KEY=your-midjourney-key
   STABLE_DIFFUSION_API_KEY=your-sd-key
   ```

5. **Initialize the database**
   ```bash
   python
   from app import db, create_app
   app = create_app()
   with app.app_context():
       db.create_all()
   ```

6. **Run the application**
   ```bash
   python app.py
   ```
   Access at `http://localhost:5000`

## Usage

1. **Register/Login** - Create an account or login
2. **Add API Keys** - Go to profile and add your API keys
3. **Generate Images** - Select model, enter prompt, click Generate
4. **View History** - Track all generated images in your profile

## API Endpoints

- `POST /api/generate` - Generate image
- `GET /api-keys` - Get user API keys
- `POST /api-keys` - Add/update API key
- `GET /auth/login` - Login page
- `POST /auth/login` - Login submission
- `POST /auth/logout` - Logout

## Technologies Used

**Backend:**
- Flask 2.3.3
- SQLAlchemy (ORM)
- Flask-Login (Authentication)
- Werkzeug (WSGI utilities)
- bcrypt (Password hashing)
- python-dotenv (Environment config)

**Frontend:**
- HTML5
- Modern CSS3 (Flexbox, Grid)
- Vanilla JavaScript
- Responsive design

**Database:**
- SQLite (Development)
- PostgreSQL (Production)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue on GitHub.

---

**Made with ❤️ for AI enthusiasts**
