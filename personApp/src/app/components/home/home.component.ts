import { Component } from '@angular/core';
import { ProjectService } from '../../services/project.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  constructor(public projectService: ProjectService) {}

  public remove(id: number) {
    if (confirm('Are you sure?')) {
      this.projectService.Remove(id);
    }
  }

}
