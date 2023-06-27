import {Symbol} from "./Symbol";
import {PyError} from "./PyError";
import {ReportType} from "./ReportType";

export class ReportModel{

  cstContent: string = '';
  output: string = '';
  c3d: string = '';
  symbol_table : Symbol[] = [];
  errors: PyError[] = [];

  private static reportModel: ReportModel | null = null;

  private constructor() {

  }

  public static getInstance(): ReportModel{
    if(this.reportModel == null){
      this.reportModel = new ReportModel();
    }
    return this.reportModel;
  }


}
