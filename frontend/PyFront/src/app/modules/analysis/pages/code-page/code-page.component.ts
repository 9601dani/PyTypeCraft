import {Component, OnInit} from '@angular/core';
import {CodeModel} from "@ngstack/code-editor";
import {RestService} from "../../services/rest.service";
import {ReportModel} from "../../../../models/ReportModel";
import {OutPutType} from "../../../../models/OutPutType";
import Swal from 'sweetalert2'

@Component({
  selector: 'app-code-page',
  templateUrl: './code-page.component.html',
  styleUrls: ['./code-page.component.css']
})
export class CodePageComponent implements OnInit{

  theme = "vs";
  outValue = '';
  outPutType:OutPutType = OutPutType.CONSOLE;

  model: CodeModel = {
    language: 'typescript',
    uri: 'main.ts',
    value: ''
  };

  options = {
    contextmenu: true,
    minimap: {
      enabled: true
    }
  };

  constructor( private restService: RestService ) { }

  ngOnInit(): void {
  }

  compile(){
    let content = this.model.value;
    if (content.trim().length == 0){
      Swal.fire({
        position: 'center',
        icon: 'question',
        title: 'No se encontró nada para compilar',
        showConfirmButton: false,
        timer: 1500
      })
      return;
    }
    let body = { 'text' : content };
    // console.log(body)
    this.restService.post(body)
      .subscribe( (value : any) => {
        if(value) {
          const reportModel: ReportModel = ReportModel.getInstance();
          reportModel.symbol_table = value.table;
          // console.log(reportModel.symbol_table)
          reportModel.errors = value.errors;
          // console.log(reportModel.errors)
          reportModel.cstContent = value.cst;
          // console.log(reportModel.cstContent)
          reportModel.c3d = value.c3d;
          reportModel.output = ''
          value.console.forEach((it: any) => {
            reportModel.output = reportModel.output.concat(it).concat("\n");
          })

          this.outValue = reportModel.output;
          this.outPutType = OutPutType.CONSOLE;
          Swal.fire({
            position: 'center',
            icon: 'success',
            title: 'Compilación realizada con éxito',
            showConfirmButton: false,
            timer: 1500
          })

        }
      })

  }

  changeOut(out: OutPutType){
    this.outPutType = out;
    if (this.outPutType === OutPutType.CONSOLE) {
      this.outValue = ReportModel.getInstance().output;
    } else if (this.outPutType === OutPutType.C3D) {
      this.outValue = ReportModel.getInstance().c3d;
    }
  }

  protected readonly OutPutType = OutPutType;
}
