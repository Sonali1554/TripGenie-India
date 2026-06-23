# TripGenie India 🇮🇳

AI-powered travel planning system built using Python, Streamlit, Ollama and a Multi-Agent Architecture.

## Features

- Profile Extraction Agent
- Research Agent
- Planner Agent
- Weather Agent
- Hotel Agent
- Budget Agent
- Packing Checklist Agent
- PDF Report Generator

## Tech Stack

- Python
- Streamlit
- Ollama
- Qwen
- ReportLab

## Architecture

User Query
↓
Profile Agent
↓
Research Agent
↓
Travel Supervisor
├── Planner Agent
├── Weather Agent
├── Hotel Agent
├── Budget Agent
└── Packing Agent
↓
PDF Generator
↓
Streamlit Dashboard