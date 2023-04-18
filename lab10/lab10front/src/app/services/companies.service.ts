import {Injectable} from '@angular/core';
import {Company} from "../models/models";
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class CompaniesService {
  BASE_URL = "http://127.0.0.1:8000/"

  constructor(private CompanyClient: HttpClient) {
  }

  getCompanies(): Observable<Company[]> {
    return this.CompanyClient.get<Company[]>(`${this.BASE_URL}api/companies/`);
  }

  createCompany(company: { name: string, description: string, city: string, address: string }): Observable<Company[]> {
    return this.CompanyClient.post<Company[]>(`${this.BASE_URL}api/companies/`, company);
  }

  deleteCompany(id:number){
    return this.CompanyClient.delete(`${this.BASE_URL}/api/companies/${id}/`);
  }
}
