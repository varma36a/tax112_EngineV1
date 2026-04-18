import { Component } from '@angular/core';
import { TaxService } from 'src/services/tax.services';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  selectedFile: File | null = null;

  result: any = null;
  preview: any[] = [];

  chartLabels: string[] = [];
  chartData: number[] = [];

  loading = false;
  error = '';

  constructor(private taxService: TaxService) { }

  // 📂 File select
  onFileChange(event: any) {
    this.selectedFile = event.target.files[0];
  }

  // 🚀 Upload + API call
  upload() {
    if (!this.selectedFile) {
      alert('Please select a file');
      return;
    }

    this.loading = true;
    this.error = '';

    this.taxService.uploadTB(this.selectedFile).subscribe({
      next: (res: any) => {
        this.result = res.result;
        this.preview = res.preview;
        this.prepareChart();
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.error = 'Upload failed. Please try again.';
        this.loading = false;
      }
    });
  }

  recalculate() {

    let revenue = 0;
    let deductions = 0;

    this.preview.forEach((row: any) => {

      if (row.category === 'revenue') {
        revenue += Math.abs(row.amount);
      }

      else if (row.category === 'expense') {
        deductions += row.amount;
      }

      else if (row.category === 'disallowed') {
        // ignore disallowed expenses
      }
    });

    const taxable = revenue - deductions;

    this.result = {
      gross_receipts: revenue,
      deductions: deductions,
      taxable_income: taxable,
      tax: taxable * 0.21
    };

    // 🔄 refresh chart after recalculation
    this.prepareChart();
  }

  // 📊 Prepare chart data
  prepareChart() {
    const map: { [key: string]: number } = {};

    this.preview.forEach((row: any) => {
      if (!map[row.category]) {
        map[row.category] = 0;
      }
      map[row.category] += Math.abs(row.amount);
    });

    this.chartLabels = Object.keys(map);
    this.chartData = Object.values(map);
  }

  // ✏️ Manual category correction (important for ML improvement)
  updateCategory(row: any, newCategory: string) {
    row.category = newCategory;
    this.prepareChart();
  }

  // 🎨 Confidence badge color
  getConfidenceClass(conf: number): string {
    if (conf > 0.8) return 'high';
    if (conf > 0.5) return 'medium';
    return 'low';
  }
}