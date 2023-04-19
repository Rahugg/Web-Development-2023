import {Component, OnInit} from '@angular/core';
import {CompaniesService} from "../../services/companies.service";
import {VacanciesService} from "../../services/vacancies.service";
import {Company} from "../../models/models";

@Component({
  selector: 'app-createvacancy',
  templateUrl: './createvacancy.component.html',
  styleUrls: ['./createvacancy.component.css']
})
export class CreatevacancyComponent implements OnInit {
  // company={
  //   name
  //
  // }

  vacancy = {
    name: '',
    description: '',
    salary: 0,
    company: null,
  };

  Companies: Company[] = []

  constructor(private vacancyService: VacanciesService, private companyService: CompaniesService) {
  }

  createVacancy() {

    this.vacancyService.createVacancy(this.vacancy).subscribe((response: any) => {
      console.log(this.vacancy)
      console.log(response);
    })
  }

  ngOnInit(): void {
    this.companyService.getCompanies().subscribe((data) => {
      console.log(data);
      this.Companies = data;
    })
  }
}
