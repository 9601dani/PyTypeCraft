import {Component, OnInit} from '@angular/core';
import {CodeModel} from "@ngstack/code-editor";

@Component({
  selector: 'app-code-page',
  templateUrl: './code-page.component.html',
  styleUrls: ['./code-page.component.css']
})
export class CodePageComponent implements OnInit{

  theme = "vs";

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
  ngOnInit(): void {
  }



}
