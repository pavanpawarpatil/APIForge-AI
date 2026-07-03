from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate

class ProjectService:
    """
    Handles all business logic related to project
    """
    
    @staticmethod
    def create_project(db: Session, project: ProjectCreate) -> Project:
        new_project = Project(
            project_name=project.project_name,
            framework=project.framework,
            database=project.database,
            llm=project.llm,
        )
        
        db.add(new_project)
        db.commit()
        db.refresh(new_project)

        return new_project
    
    @staticmethod
    def get_all_projects(db: Session):
        return db.query(Project).all()

    @staticmethod
    def get_project_by_id(db: Session, project_id: int):
        return (
            db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

    @staticmethod
    def delete_project(db: Session, project_id: int):
        project = (
            db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

        if project:
            db.delete(project)
            db.commit()

        return project