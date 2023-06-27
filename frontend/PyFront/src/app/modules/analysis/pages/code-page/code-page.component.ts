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
          reportModel.output = ''
          value.console.forEach((it: any) => {
            reportModel.output = reportModel.output.concat(it).concat("\n");
          })

          this.outValue = reportModel.output;
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

  getC3D(){
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
    let out = "";
    let body = { 'text' : content };
    this.restService.c3d_post(body)
      .subscribe((value: any) =>{
        if(value){
           this.outValue = value.c3d;
        }
      })
    Swal.fire({
      position: 'center',
      icon: 'success',
      title: 'Compilación realizada con éxito',
      showConfirmButton: false,
      timer: 1500
    })
  }
}
