# Django 6.0 Modern Stack

A modern web application stack featuring Django 6.0 beta with a cutting-edge frontend setup.

## Tech Stack

- **Backend**: Django 6.0 (beta) + Gunicorn
- **Frontend CSS**: Tailwind CSS 4.1 (compiled, not CDN)
- **Frontend JS**:
  - HTMX 2.0 (local)
  - Alpine.js 3.14 (local)
  - Flowbite 3.1 (local)
- **Static Files**: WhiteNoise

All JavaScript libraries are served locally - no CDN dependencies!

## Prerequisites

- Python 3.12+
- Node.js 22+ and npm

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd claude_code
   ```

2. **Set up Python virtual environment**
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Node.js dependencies**
   ```bash
   npm install
   ```

5. **Copy JavaScript files to static directory**
   ```bash
   npm run copy-js
   ```

6. **Build Tailwind CSS**
   ```bash
   npm run build
   ```

7. **Run migrations**
   ```bash
   python manage.py migrate
   ```

## Development

### Run the development server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see the demo page.

### Watch Tailwind CSS changes

In a separate terminal:
```bash
npm run dev
```

This will watch for changes in your templates and rebuild Tailwind CSS automatically.

## Production Deployment

### Build static files

```bash
npm run build
python manage.py collectstatic --noinput
```

### Run with Gunicorn

```bash
gunicorn config.wsgi --bind 0.0.0.0:8000
```

Or use the Procfile for platforms like Heroku:
```bash
web: gunicorn config.wsgi --log-file -
```

## Project Structure

```
.
├── config/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                # Main Django app
│   ├── templates/
│   │   └── core/
│   │       └── index.html
│   ├── views.py
│   └── urls.py
├── static/
│   ├── src/
│   │   └── input.css    # Tailwind source
│   ├── dist/
│   │   └── output.css   # Compiled Tailwind
│   └── js/              # Local JS libraries
│       ├── htmx.min.js
│       ├── alpine.min.js
│       └── flowbite.min.js
├── package.json         # Node dependencies
├── tailwind.config.js   # Tailwind configuration
├── requirements.txt     # Python dependencies
└── manage.py
```

## Features Demonstrated

The demo page (`/`) showcases:

1. **Tailwind CSS 4.1** - Modern utility-first CSS with custom configuration
2. **HTMX** - Dynamic form submission without page refresh
3. **Alpine.js** - Reactive components (counter, toggle)
4. **Flowbite** - Pre-built UI components (navbar, alerts)
5. **Django 6.0** - Latest Django features and improvements

## Django Cotton

django-cotton is included in the dependencies for component-based templates. While there's a version compatibility warning with Django 6.0 beta, it's installed and ready to use. You can create reusable components in your templates.

## NPM Scripts

- `npm run build` - Build Tailwind CSS for production (minified)
- `npm run dev` - Watch mode for Tailwind CSS development
- `npm run copy-js` - Copy JS libraries from node_modules to static/js

## Environment Variables

Copy `.env.example` to `.env` and configure:

```
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Notes

- Django 6.0 is currently in beta. For production, consider using Django 5.2 LTS.
- All JavaScript libraries are bundled locally for better performance and offline development.
- Tailwind CSS is compiled at build time, not loaded via CDN.

## License

MIT
