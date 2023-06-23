import {Component, OnInit} from '@angular/core';
import {CodeModel} from "@ngstack/code-editor";
import {RestService} from "../../services/rest.service";

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
    let body = { 'text' : content };
    console.log(body)
    this.restService.post(body)
      .subscribe( (value : any) => {
        if(value){
          console.log(value);
          let console_result = ''
          value.console.forEach((it: any) =>{
            console_result = console_result + it +"\n"
          })
          this.outValue = console_result;
        }
      } )

  }


}
