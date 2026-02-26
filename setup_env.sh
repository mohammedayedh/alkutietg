#!/bin/bash

# Script to setup .env file on server
# Run this after git pull

ENV_FILE="/srv/alkutietg/app/.env"

# Check if .env exists
if [ -f "$ENV_FILE" ]; then
    echo ".env file already exists"
    exit 0
fi

# Create .env file
cat > "$ENV_FILE" << 'EOF'
SECRET_KEY=django-insecure-change-this-in-production-alkutietg-2024
DEBUG=False
ALLOWED_HOSTS=alkutietg.com,www.alkutietg.com,72.61.96.17,localhost,127.0.0.1

DB_ENGINE=django.db.backends.postgresql
DB_NAME=alkutietg_db
DB_USER=alkutietg_user
DB_PASSWORD=p2x4pD9R6Y--
DB_HOST=localhost
DB_PORT=5432

STATIC_URL=/static/
STATIC_ROOT=/srv/alkutietg/app/staticfiles
MEDIA_URL=/media/
MEDIA_ROOT=/srv/alkutietg/app/media
EOF

echo ".env file created successfully"
chmod 600 "$ENV_FILE"
chown alkutietg:alkutietg "$ENV_FILE"
