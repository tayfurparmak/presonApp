import { Component } from '@angular/core';
import { ProjectService } from '../../services/project.service';

@Component({
  selector: 'app-person-create',
  templateUrl: './person-create.component.html',
  styleUrl: './person-create.component.css'
})
export class PersonCreateComponent {
  public project: any = {};

  constructor(
    private projectService: ProjectService,

  ) {}

  save() {
    this.projectService.Add(this.project);
    this.project = {};

  }
}
