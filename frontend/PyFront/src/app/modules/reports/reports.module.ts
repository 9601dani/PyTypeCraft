import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReportsRoutingModule } from './reports-routing.module';
import { ReportPageComponent } from './pages/report-page/report-page.component';
import {SharedModule} from "../../shared/shared.module";


@NgModule({
  declarations: [
    ReportPageComponent
  ],
    imports: [
        CommonModule,
        ReportsRoutingModule,
        SharedModule
    ]
})
export class ReportsModule { }
