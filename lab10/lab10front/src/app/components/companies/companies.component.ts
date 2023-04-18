import {Component, OnInit} from '@angular/core';
import {Company} from "../../models/models";
import {CompaniesService} from "../../services/companies.service";

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent implements OnInit {

  Companies: Company[] = []

  constructor(private companyService: CompaniesService) {
  }

  ngOnInit(): void {
    this.companyService.getCompanies().subscribe((data) => {
      console.log(data);
      this.Companies = data;
    })
  }

}
