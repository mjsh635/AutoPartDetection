namespace Auto_Part_Detection_Debug_App
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.CheckAllTags = new System.Windows.Forms.Button();
            this.ReadAllTags = new System.Windows.Forms.Button();
            this.ReadTagFromDockNum = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.dock1TB = new System.Windows.Forms.TextBox();
            this.dock2TB = new System.Windows.Forms.TextBox();
            this.dock3TB = new System.Windows.Forms.TextBox();
            this.dock4TB = new System.Windows.Forms.TextBox();
            this.dock5TB = new System.Windows.Forms.TextBox();
            this.dock6TB = new System.Windows.Forms.TextBox();
            this.dock7TB = new System.Windows.Forms.TextBox();
            this.dock8TB = new System.Windows.Forms.TextBox();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.SuspendLayout();
            // 
            // CheckAllTags
            // 
            this.CheckAllTags.Location = new System.Drawing.Point(570, 243);
            this.CheckAllTags.Name = "CheckAllTags";
            this.CheckAllTags.Size = new System.Drawing.Size(181, 60);
            this.CheckAllTags.TabIndex = 0;
            this.CheckAllTags.Text = "Check All Tags";
            this.CheckAllTags.UseVisualStyleBackColor = true;
            this.CheckAllTags.Click += new System.EventHandler(this.CheckAllTags_Click);
            // 
            // ReadAllTags
            // 
            this.ReadAllTags.Location = new System.Drawing.Point(570, 176);
            this.ReadAllTags.Name = "ReadAllTags";
            this.ReadAllTags.Size = new System.Drawing.Size(181, 60);
            this.ReadAllTags.TabIndex = 1;
            this.ReadAllTags.Text = "Read All Tags";
            this.ReadAllTags.UseVisualStyleBackColor = true;
            this.ReadAllTags.Click += new System.EventHandler(this.ReadAllTags_Click);
            // 
            // ReadTagFromDockNum
            // 
            this.ReadTagFromDockNum.Location = new System.Drawing.Point(570, 12);
            this.ReadTagFromDockNum.Name = "ReadTagFromDockNum";
            this.ReadTagFromDockNum.Size = new System.Drawing.Size(181, 60);
            this.ReadTagFromDockNum.TabIndex = 2;
            this.ReadTagFromDockNum.Text = "Read Tag From Dock ";
            this.ReadTagFromDockNum.UseVisualStyleBackColor = true;
            this.ReadTagFromDockNum.Click += new System.EventHandler(this.ReadTagFromDockNum_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(27, 12);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(79, 25);
            this.label1.TabIndex = 3;
            this.label1.Text = "Dock 1";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(27, 54);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(79, 25);
            this.label2.TabIndex = 4;
            this.label2.Text = "Dock 2";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(27, 96);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(79, 25);
            this.label3.TabIndex = 5;
            this.label3.Text = "Dock 3";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(27, 138);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(79, 25);
            this.label4.TabIndex = 6;
            this.label4.Text = "Dock 4";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(27, 180);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(79, 25);
            this.label5.TabIndex = 7;
            this.label5.Text = "Dock 5";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(27, 222);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(79, 25);
            this.label6.TabIndex = 8;
            this.label6.Text = "Dock 6";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(27, 264);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(79, 25);
            this.label7.TabIndex = 9;
            this.label7.Text = "Dock 7";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(27, 306);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(79, 25);
            this.label8.TabIndex = 10;
            this.label8.Text = "Dock 8";
            // 
            // dock1TB
            // 
            this.dock1TB.Location = new System.Drawing.Point(112, 12);
            this.dock1TB.Name = "dock1TB";
            this.dock1TB.ReadOnly = true;
            this.dock1TB.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.dock1TB.Size = new System.Drawing.Size(452, 31);
            this.dock1TB.TabIndex = 11;
            // 
            // dock2TB
            // 
            this.dock2TB.Location = new System.Drawing.Point(112, 54);
            this.dock2TB.Name = "dock2TB";
            this.dock2TB.ReadOnly = true;
            this.dock2TB.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.dock2TB.Size = new System.Drawing.Size(452, 31);
            this.dock2TB.TabIndex = 12;
            // 
            // dock3TB
            // 
            this.dock3TB.Location = new System.Drawing.Point(112, 96);
            this.dock3TB.Name = "dock3TB";
            this.dock3TB.ReadOnly = true;
            this.dock3TB.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.dock3TB.Size = new System.Drawing.Size(452, 31);
            this.dock3TB.TabIndex = 13;
            // 
            // dock4TB
            // 
            this.dock4TB.Location = new System.Drawing.Point(112, 138);
            this.dock4TB.Name = "dock4TB";
            this.dock4TB.ReadOnly = true;
            this.dock4TB.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.dock4TB.Size = new System.Drawing.Size(452, 31);
            this.dock4TB.TabIndex = 14;
            // 
            // dock5TB
            // 
            this.dock5TB.Location = new System.Drawing.Point(112, 180);
            this.dock5TB.Name = "dock5TB";
            this.dock5TB.ReadOnly = true;
            this.dock5TB.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.dock5TB.Size = new System.Drawing.Size(452, 31);
            this.dock5TB.TabIndex = 15;
            // 
            // dock6TB
            // 
            this.dock6TB.Location = new System.Drawing.Point(112, 222);
            this.dock6TB.Name = "dock6TB";
            this.dock6TB.ReadOnly = true;
            this.dock6TB.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.dock6TB.Size = new System.Drawing.Size(452, 31);
            this.dock6TB.TabIndex = 16;
            // 
            // dock7TB
            // 
            this.dock7TB.Location = new System.Drawing.Point(112, 264);
            this.dock7TB.Name = "dock7TB";
            this.dock7TB.ReadOnly = true;
            this.dock7TB.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.dock7TB.Size = new System.Drawing.Size(452, 31);
            this.dock7TB.TabIndex = 17;
            // 
            // dock8TB
            // 
            this.dock8TB.Location = new System.Drawing.Point(112, 306);
            this.dock8TB.Name = "dock8TB";
            this.dock8TB.ReadOnly = true;
            this.dock8TB.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.dock8TB.Size = new System.Drawing.Size(452, 31);
            this.dock8TB.TabIndex = 18;
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Items.AddRange(new object[] {
            "Dock 1",
            "Dock 2",
            "Dock 3",
            "Dock 4",
            "Dock 5",
            "Dock 6",
            "Dock 7",
            "Dock 8"});
            this.comboBox1.Location = new System.Drawing.Point(570, 78);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(181, 33);
            this.comboBox1.TabIndex = 19;
            this.comboBox1.Tag = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(12F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ControlLight;
            this.ClientSize = new System.Drawing.Size(792, 368);
            this.Controls.Add(this.comboBox1);
            this.Controls.Add(this.dock8TB);
            this.Controls.Add(this.dock7TB);
            this.Controls.Add(this.dock6TB);
            this.Controls.Add(this.dock5TB);
            this.Controls.Add(this.dock4TB);
            this.Controls.Add(this.dock3TB);
            this.Controls.Add(this.dock2TB);
            this.Controls.Add(this.dock1TB);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.ReadTagFromDockNum);
            this.Controls.Add(this.ReadAllTags);
            this.Controls.Add(this.CheckAllTags);
            this.Name = "Form1";
            this.Text = "Tag Reader";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button CheckAllTags;
        private System.Windows.Forms.Button ReadAllTags;
        private System.Windows.Forms.Button ReadTagFromDockNum;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.TextBox dock1TB;
        private System.Windows.Forms.TextBox dock2TB;
        private System.Windows.Forms.TextBox dock3TB;
        private System.Windows.Forms.TextBox dock4TB;
        private System.Windows.Forms.TextBox dock5TB;
        private System.Windows.Forms.TextBox dock6TB;
        private System.Windows.Forms.TextBox dock7TB;
        private System.Windows.Forms.TextBox dock8TB;
        private System.Windows.Forms.ComboBox comboBox1;
    }
}

