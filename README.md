# SOLID Principles: Student Management System
![Python CI Pipeline](https://github.com/danimarpas4/Base_de_datos_Estudiantes_SOLID/actions/workflows/ci.yml/badge.svg)

> A modular Python architecture demonstrating robust software design patterns applied to a database-driven application.

## ⚡ Overview
This project simulates a backend system for managing student records. Instead of a monolithic script, I've deconstructed the logic to strictly follow **SOLID Principles**. This ensures the codebase is scalable, maintainable, and ready for future iterations (like migrating to a distributed ledger or a microservices architecture).

## 🛠 Tech Stack
* **Core:** Python 3.12+
* **ORM:** SQLAlchemy (Abstracting the Data Layer)
* **Database:** SQLite (Local development) / Scalable to PostgreSQL

## 🧩 Architecture Modules
Each module represents a core design principle:
* **SRP (`SingleResponsibilityPrinciple.py`):** Decoupling Data Entities (`Estudiante`) from Persistence Logic (`EstudiantesBD`).
* **OCP (`OpenClosedPrinciple.py`):** Scholarship logic is open for extension (new rules) but closed for modification.
* **LSP (`LiskovSubstitutionPrinciple.py`):** Polymorphic notification channels (Email/SMS) interchangeable at runtime.
* **ISP (`InterfaceSegregationPrinciple.py`):** Clients only depend on the reporting interfaces they actually use.
* **DIP (`DependencyInversionPrinciple.py`):** High-level modules depend on abstractions (Database Interface), not low-level implementation details.

## 🚀 Quick Start

1.  **Environment Setup**
    ```bash
    pip install sqlalchemy python-dotenv
    ```

2.  **Deploy Logic**
    ```bash
    python main.py
    ```