# Ultimate Health Center

One-stop online health and wellness platform.

This repo is an early scaffold for:
- A FastAPI backend with:
  - A small open-source chat model (TinyLlama 1.1B Chat) for a health assistant endpoint.[web:17][web:18][web:19]
  - Stripe Checkout + webhook endpoints for paid add-ons (e.g., premium programs, partner tools).[web:22][web:28][web:31]
  - SQLModel-based database with auth, professionals, programs, and products APIs.[web:40][web:41][web:44]
- Future front-end (React/Next.js or similar) that talks to this API.

## Stack
- Python 3.11+
- FastAPI + Uvicorn
- SQLModel + SQLite (default)
- Stripe Python SDK
- TinyLlama 1.1B Chat via `transformers` or `llama-cpp-python` (you can swap to another small open-source model).[web:17][web:24]

## Getting started

1. Clone the repo:
   ```bash
   git clone https://github.com/ncsound919/ultimate-health-center.git
   cd ultimate-health-center
   ```

2. Create and activate a virtualenv (optional but recommended).

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and fill in:
   - `STRIPE_SECRET_KEY`
   - `STRIPE_WEBHOOK_SECRET`
   - `DOMAIN` (e.g. http://localhost:8000)
   - `DATABASE_URL` (or use the default SQLite path)
   - `JWT_SECRET_KEY` and `JWT_ALGORITHM`
   - `MODEL_BACKEND` ("transformers" or "llama_cpp")
   - `MODEL_NAME` (e.g. TinyLlama/TinyLlama-1.1B-Chat-v1.0)

5. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```

## API overview (initial)
- `POST /api/chat` — proxy to the local small open-source model for simple health/wellness Q&A.
- `POST /api/create-checkout-session` — create a Stripe Checkout session for a sample product.
- `POST /api/stripe/webhook` — receive Stripe webhooks.
- `POST /api/auth/register` — register a new user with email, name, and password.
- `POST /api/auth/token` — obtain a JWT access token via OAuth2 password flow.
- `GET /api/auth/me` — get the current authenticated user.
- `POST /api/core/professionals` / `GET /api/core/professionals` — create and list professional profiles (for the doctor/trainer registry).
- `POST /api/core/programs` / `GET /api/core/programs` — create and list programs (meal/workout/mental health paths).
- `POST /api/core/products` / `GET /api/core/products` — create and list products (vitamins, herbal remedies, kits, etc.).

From here you can add:
- User roles and verification flows for professionals.
- Detailed schemas for plans, content, and appointments.
- UI in a separate front-end app.
