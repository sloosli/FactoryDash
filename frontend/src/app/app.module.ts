import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import {MainModule} from "./main/main.module";
import {RouterModule, Routes} from "@angular/router";
import {MainComponent} from "./main/main.component";
import {SchedulePlanModule} from "./schedule-plan/schedule-plan.module";
import {SchedulePlanComponent} from "./schedule-plan/shedule-plan.component";
import {HttpClientModule} from "@angular/common/http";

const appRoutes: Routes =[
  { path: '', component: MainComponent},
  { path: 'schedule-plan', component: SchedulePlanComponent},
];

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes),
    MainModule,
    SchedulePlanModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
