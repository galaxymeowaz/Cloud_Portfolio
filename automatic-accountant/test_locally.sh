#!/bin/bash
# ==============================================================================
# Automatic Accountant - Local Testing Script
# Created by Joseph Tay (aztay.org) | Copyright (c) 2026
# Licensed under the MIT License.
# ==============================================================================
# Local execution and testing script for DevOps workflows
set -e

echo "======================================"
echo " AWS Lambda Local Test Runner"
echo "======================================"

if [ ! -f "credentials.json" ]; then
    echo "❌ ERROR: credentials.json not found! Please download your Google Service Account key."
    exit 1
fi

if [ ! -f ".env" ]; then
    echo "⚠️ WARNING: .env not found. Copying .env.example -> .env"
    cp .env.example .env
fi

echo "🐳 Building Docker Image..."
docker compose build

echo ""
echo "▶️ Testing EventBridge Schedule (calendar_sync.py)..."
docker compose run --rm ledger_sync_test

echo ""
echo "✅ Local testing completed successfully!"
