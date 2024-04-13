from random import randint, choice as rc
from app import app
from models import db, Projects
import json
from faker import Faker
fake = Faker()


def create_projects():
    projects = []
    projects_list = [
        {
            "name" : "PennyWise",
            "description" : "An ios application that allows users to create a monthly savings plan and categorically track expenses",
            "link" : "https://github.com/ckim97/pennywise",
            "demo" : "https://www.loom.com/share/a748719b48d34b379b8530dfbcb8e7ff",
            "stack" : ["Flutter", "Dart", "Flask", "SQlAlchemy", "Firebase"]
        },
        {
            "name" : "JoyRide",
            "description" : "An online space for event attendees to organize carpools",
            "link" : "https://github.com/cpburns17/project-concert-rideshare",
            "demo" : "https://www.loom.com/share/d7413911798349c78896e0ba9216778e",
            "stack" : ["React.js", "CSS", "Bootstrap", "Python", "Flask", "SQLAlchemy"]
        },
        {
            "name" : "Space Shooter",
            "description" : "A basic “neverending” shooting game utilizing an infinitely scrolling screen",
            "link" : "https://github.com/ckim97/phase-3-space-game",
            "demo" : "https://www.loom.com/share/03f36e890b1d4b06a82943fb9ffb1cdd",
            "stack" : ["Python", "Pygames"]
        },
        {
            "name" : "Barbershop Project",
            "description" : "A website designed for barbershops to upload their services and patients to book appointments",
            "link" : "https://github.com/ckim97/barber-project-phase-2",
            "demo" : "https://www.loom.com/share/dfb0afea2eca447bb353fd8596e40eec",
            "stack" : ["React.js", "CSS"]
        }
    ]

    for project in projects_list:
        p = Projects(
            name = project["name"],
            description = project["description"],
            link = project["link"],
            demo = project["demo"],
            stack = json.dumps(project["stack"])
        )
        projects.append(p)

    # for _ in range(4):
    #     p = Projects(
    #         name = fake.name(),
    #         link = fake.url(),
    #         description = fake.sentence(nb_words=5),
    #         stack = fake.sentence(nb_words=5)
    #     )
    #     projects.append(p)
    
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