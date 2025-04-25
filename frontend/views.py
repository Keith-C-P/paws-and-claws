from flet import Page, View
from employee_add import EmployeeAdd
from pet_surfer import PetSurfer
from shelter_sign_up import ShelterSignUp
from adopter_sign_up import AdopterSignUp
from login import Login
from choice import Choice

def view_handler(page: Page) -> dict[str, View]:
    return {
        '/adopter-sign-up': AdopterSignUp(page), 
        '/shelter-sign-up': ShelterSignUp(page=page),
        '/pet-surfer': PetSurfer(page=page),
        '/add-employee': EmployeeAdd(page=page),
        '/login': Login(page),
        '/': Choice(page)
    }