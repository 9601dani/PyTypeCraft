import {Component, OnInit} from '@angular/core';
import {ReportType} from "../../../../models/ReportType";

@Component({
  selector: 'app-report-page',
  templateUrl: './report-page.component.html',
  styleUrls: ['./report-page.component.css']
})
export class ReportPageComponent implements OnInit{
  reportType:ReportType = ReportType.NONE;

  ngOnInit(): void {
  }

  changeReport(report: ReportType){
    this.reportType = report;
  }

  protected readonly ReportType = ReportType;
}
