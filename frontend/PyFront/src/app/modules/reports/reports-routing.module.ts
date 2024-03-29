import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {ReportPageComponent} from "./pages/report-page/report-page.component";

const routes: Routes = [
  {
    path: '',
    component: ReportPageComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ReportsRoutingModule { }
