import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {CompaniesComponent} from './components/companies/companies.component';
import {HomeComponent} from './components/home/home.component';
import {VacanciesComponent} from './components/vacancies/vacancies.component';
import {NavbarComponent} from './components/navbar/navbar.component';
import {HttpClientModule} from "@angular/common/http";
import { CreatecompanyComponent } from './components/createcompany/createcompany.component';
import { CreatevacancyComponent } from './components/createvacancy/createvacancy.component';
import {FormsModule} from "@angular/forms";

@NgModule({
  declarations: [
    AppComponent,
    CompaniesComponent,
    HomeComponent,
    VacanciesComponent,
    NavbarComponent,
    CreatecompanyComponent,
    CreatevacancyComponent,

  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        FormsModule
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
