using System;
using Windows.Foundation;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;

namespace TemplateFlutter.UwpShell
{
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            InitializeComponent();
            View.NavigationStarting += OnNavigationStarting;
            View.NavigationCompleted += OnNavigationCompleted;
            View.Navigate(new Uri("ms-appx-web:///Assets/index.html"));
        }

        void OnNavigationStarting(WebView sender, WebViewNavigationStartingEventArgs e)
        {
            if (e.Uri.Scheme != "ms-appx-web") e.Cancel = true;
        }

        void OnNavigationCompleted(WebView sender, WebViewNavigationCompletedEventArgs e)
        {
            if (!e.IsSuccess) View.Navigate(new Uri("ms-appx-web:///Assets/index.html"));
        }
    }
}
