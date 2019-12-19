import sys
from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    """Seeds the database with test data."""
    db.session.add(User(username='trey', email='trey@nope.com'))
    db.session.add(User(username='robin', email='robin@nope.com'))
    db.session.commit()
    
if __name__ == '__main__':
    cli()