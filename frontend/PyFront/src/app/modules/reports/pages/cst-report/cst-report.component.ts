import {Component, OnInit} from '@angular/core';
import {ReportModel} from "../../../../models/ReportModel";
import { graphviz } from "d3-graphviz"


@Component({
  selector: 'app-cst-report',
  templateUrl: './cst-report.component.html',
  styleUrls: ['./cst-report.component.css']
})
export class CstReportComponent implements OnInit{
  ngOnInit(): void {
    graphviz("#graph")
      .renderDot(ReportModel.getInstance().cstContent)
  }

}
