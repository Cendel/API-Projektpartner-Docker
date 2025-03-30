#!/bin/sh

# PostgreSQL'in hazır olmasını bekle
echo "📡 Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.5
done

echo "✅ Postgres is ready. Starting Django..."

exec "$@"
