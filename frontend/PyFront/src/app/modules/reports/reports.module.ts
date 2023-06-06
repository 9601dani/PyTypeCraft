import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReportsRoutingModule } from './reports-routing.module';
import { ReportPageComponent } from './pages/report-page/report-page.component';
import {SharedModule} from "../../shared/shared.module";
import { ErrorReportComponent } from './pages/error-report/error-report.component';
import { TableReportComponent } from './pages/table-report/table-report.component';
import { AstReportComponent } from './pages/ast-report/ast-report.component';


@NgModule({
  declarations: [
    ReportPageComponent,
    ErrorReportComponent,
    TableReportComponent,
    AstReportComponent
  ],
    imports: [
        CommonModule,
        ReportsRoutingModule,
        SharedModule
    ]
})
export class ReportsModule { }
