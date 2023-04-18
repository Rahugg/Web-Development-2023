import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {HomeComponent} from "./components/home/home.component";
import {CompaniesComponent} from "./components/companies/companies.component";
import {VacanciesComponent} from "./components/vacancies/vacancies.component";
import {CreatecompanyComponent} from "./components/createcompany/createcompany.component";
import {CreatevacancyComponent} from "./components/createvacancy/createvacancy.component";

const routes: Routes = [
  {path: 'home', component: HomeComponent},
  {path: 'companies', component: CompaniesComponent},
  {path: 'vacancies', component: VacanciesComponent},
  {path: '', component: HomeComponent},
  {path: 'createcompany', component: CreatecompanyComponent},
  {path: 'createvacancy', component: CreatevacancyComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
