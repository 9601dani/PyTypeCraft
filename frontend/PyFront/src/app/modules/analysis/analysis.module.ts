import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AnalysisRoutingModule } from './analysis-routing.module';
import { CodePageComponent } from './pages/code-page/code-page.component';
import {SharedModule} from "../../shared/shared.module";
import {CodeEditorModule} from "@ngstack/code-editor";
import {RestService} from "./services/rest.service";


@NgModule({
  declarations: [
    CodePageComponent
  ],
  imports: [
    CommonModule,
    AnalysisRoutingModule,
    SharedModule,
    CodeEditorModule
  ]
})
export class AnalysisModule { }
