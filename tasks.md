# Corporation
### Case study task for a job interview

**Objective**: Build a Django project based on the [Cookiecutter](https://github.com/cookiecutter/cookiecutter-django) Django template that includes creating and managing a corporation model linked to the user model. Each task should be committed incrementally, with the final project pushed to a GitHub repository.  

**Steps**:  
1. **Set up the Project**  

   - Use the Cookiecutter Django template to initialize a new project  
   - Configure the project environment to ensure it runs locally.
2. **Create a New Django App**  
   - Name the app as corporations or similar.
   - Make sure this app is included in the Django project settings.
   - Be aware that you need to need to copy the created folder to the project base folder.  
3. **Develop the Corporation Model**  
   - Create a Corporation model with the following fields: 
     - name (CharField, required)
     - address (TextField, required)
     - url (URLField, optional)
     - Other relevant fields as needed.
   - Establish a relationship between the Corporation model and the existing User model (e.g. using a ForeignKey or OneToOneField).
   - Write a unit test that tests the corporation and user model.
4. **Create CRUD Templates**  
   - Design templates for the following views:  
     - Create: A form to create a new corporation entry.
     - Update: A form to edit an existing corporation.
     - Delete: A form or button to delete a corporation.
   - Make sure each form template provides feedback (like success or error messages).
5. **Commit Each Step**
   - Commit changes incrementally after each of the above steps, ensuring clear commit messages.
6. **Push to GitHub**
   - Create a public GitHub repository for the project.
   - Push all code with commit history to the repository.  

**Evaluation Criteria**
- Proper setup and use of Cookiecutter Django.
- Clear and functional CRUD operations for the Corporation model.
- Effective integration of the Corporation model with the User model.
- Organized commit history that reflects the task progression.