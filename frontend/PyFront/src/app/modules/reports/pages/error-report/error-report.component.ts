import { Component } from '@angular/core';
import {ReportModel} from "../../../../models/ReportModel";

@Component({
  selector: 'app-error-report',
  templateUrl: './error-report.component.html',
  styleUrls: ['./error-report.component.css']
})
export class ErrorReportComponent {

  protected readonly ReportModel = ReportModel;
}
