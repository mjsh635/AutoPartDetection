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
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text.Json;
using System.Net.Http;
using Grpc.Core;



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

            Channel channel = new Channel("127.0.0.1:50053", ChannelCredentials.Insecure);
            var client = new AutoPartDetection.AutoPartDetectionClient(channel);
            var list_of_tags_request = new Get_List_of_Tags_Request();
            list_of_tags_request.Age = 16;
            Console.WriteLine(client.Get_List_of_Tags(list_of_tags_request));
            /*bctrl.Read_dock(comboBox1.SelectedIndex+1);*/
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
           
        }
    }

    

    // YOUR CODE GOES HERE


}
