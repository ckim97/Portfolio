from random import randint, choice as rc
from app import app
from models import db, Projects
from faker import Faker
fake = Faker()

def create_projects():
    projects = []
    projects_list = [
        {
            "name" : "PennyWise",
            "description" : "An ios application that allows users to create a monthly savings plan and categorically track expenses",
            "github" : "https://github.com/ckim97/pennywise",
            "demo" : "https://www.loom.com/share/a748719b48d34b379b8530dfbcb8e7ff",
        },
        {
            "name" : "PennyWise",
            "description" : "An ios application that allows users to create a monthly savings plan and categorically track expenses",
            "github" : "https://github.com/ckim97/pennywise",
            "demo" : "https://www.loom.com/share/a748719b48d34b379b8530dfbcb8e7ff",
        },
        {
            "name" : "PennyWise",
            "description" : "An ios application that allows users to create a monthly savings plan and categorically track expenses",
            "github" : "https://github.com/ckim97/pennywise",
            "demo" : "https://www.loom.com/share/a748719b48d34b379b8530dfbcb8e7ff",
        },
        {
            "name" : "PennyWise",
            "description" : "An ios application that allows users to create a monthly savings plan and categorically track expenses",
            "github" : "https://github.com/ckim97/pennywise",
            "demo" : "https://www.loom.com/share/a748719b48d34b379b8530dfbcb8e7ff",
        }
    ]
    
    for _ in range(4):
        p = Projects(
            name = fake.name(),
            link = fake.url(),
            description = fake.sentence(nb_words=5),
            stack = fake.sentence(nb_words=5)
        )
        projects.append(p)
    
    return projects

if __name__ == '__main__':
    with app.app_context():
        print('clearing DB...')
        Projects.query.delete()

        print('Seeding Projects Table')
        projects = create_projects()
        db.session.add_all(projects)
        db.session.commit()

        print("Seeding complete!")