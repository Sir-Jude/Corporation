# Django project case study for a job interview

**Objective**: Build a Django project based on the Cookiecutter Django template that includes creating and managing a corporation model linked to the user model. Each task should be committed incrementally, with the final project pushed to a GitHub repository.

## Steps

### 1. Set up the Project
- Use the Cookiecutter Django template to initialize a new project.
- Configure the project environment to ensure it runs locally.

### 2. Create a New Django App
- Name the app as `corporations` or similar.
- Include the app in the Django project settings.
- Ensure the created app folder is copied to the project base folder.

### 3. Develop the Corporation Model
- Create a `Corporation` model with the following fields:
  - `name` (CharField, required)
  - `address` (TextField, required)
  - `url` (URLField, optional)
  - Other relevant fields as needed.
- Establish a relationship between the `Corporation` model and the existing `User` model (e.g., using a `ForeignKey` or `OneToOneField`).
- Write a unit test to test the `Corporation` and `User` models.

### 4. Create CRUD Templates
- Design templates for the following views:
  - **Create**: A form to create a new corporation entry.
  - **Update**: A form to edit an existing corporation.
  - **Delete**: A form or button to delete a corporation.
- Ensure each form template provides feedback (e.g., success or error messages).

### 5. Commit Each Step
- Commit changes incrementally after each of the above steps, ensuring clear commit messages.

### 6. Push to GitHub
- Create a public GitHub repository for the project.
- Push all code with the commit history to the repository.

## Evaluation Criteria
- Proper setup and use of Cookiecutter Django.
- Clear and functional CRUD operations for the `Corporation` model.
- Effective integration of the `Corporation` model with the `User` model.
- Organized commit history that reflects the task progression.
