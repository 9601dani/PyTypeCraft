import { Component } from '@angular/core';
import {ReportModel} from "../../../../models/ReportModel";

@Component({
  selector: 'app-table-report',
  templateUrl: './table-report.component.html',
  styleUrls: ['./table-report.component.css']
})
export class TableReportComponent {

    protected readonly ReportModel = ReportModel;

    public getValue(value: any, symbol_type: string): string{
      switch (symbol_type){
        case "VARIABLE":
          return value;
          // return this.getArrayValue(value.var)
        case "INTERFACE":
          return this.getInterfaceAttrs(value.attributes)
        default:
          return ''
      }
    }

    // public getArrayValue(value: any):string{
    //   if(value.symbol_type == "VARIABLE"){
    //     return value.value
    //   }
    //
    //   return this.getArrayValue(value.value.var)
    //   // return ''
    // }

    public getInterfaceAttrs(value: any[]){
      // console.log(value)
      let content = "{"
      value.forEach((it: any) =>{
        // console.log(it)
        content += "\""+it.id+"\":\""+it.data_type+"\","
      })
      content = content.substring(0, content.length-1);
      content+= "}"
      return content
    }
}
