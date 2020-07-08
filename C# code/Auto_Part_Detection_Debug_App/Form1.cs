using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Auto_Part_Detection_Debug_App
{
    

    public partial class Form1 : Form
    {
        object selected_val;
        ButtonControls bctrl = new ButtonControls();
        public Form1()
        {
            InitializeComponent();
            comboBox1.SelectedIndex = 0;
            
        }

        private void ReadTagFromDockNum_Click(object sender, EventArgs e)
        {
            selected_val = comboBox1.SelectedItem;
            dock1TB.Text = string.Format("read_From Specific: {0}", selected_val);
            bctrl.Read_dock(comboBox1.SelectedIndex+1);
        }

        private void ReadAllTags_Click(object sender, EventArgs e)
        {
            dock1TB.Text = "read_all";
            bctrl.Read_all_tags();
        }

        private void CheckAllTags_Click(object sender, EventArgs e)
        {
            dock1TB.Text = "read_check";
            bctrl.Check_all_tags();
        }
    }

    public class ButtonControls
    {
        public void Read_all_tags()
        {
            Console.WriteLine("read all tags");
        }

        public void Check_all_tags()
        {
            Console.WriteLine("check all tags");
        }

        public void Read_dock(int n)
        {
            Console.WriteLine("reading dock" + n);
        }
    }
}
