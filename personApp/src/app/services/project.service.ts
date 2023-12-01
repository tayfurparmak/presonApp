import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ProjectService {
  private projects: any[] = JSON.parse(
    localStorage.getItem('projects') || '[]'
  );
  public Get(): any[] {
    return this.projects;
  }
  public Add(project: any) {
    project.id = new Date().getTime();
    this.projects.push(project);
    this.Reload();
  }
  public Remove(id: number) {
    this.projects = this.projects.filter((item) => {return item.id !== id});
    this.Reload();
  }
  public Update(id: number, project: any) {
    this.Remove(id);
    project.id = id;
    this.projects.push(project);
    this.Reload();
  }
  private Reload() {
    localStorage.setItem('projects', JSON.stringify(this.projects));
  }
}
