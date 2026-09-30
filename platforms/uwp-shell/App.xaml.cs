using Windows.ApplicationModel.Activation;
using Windows.UI.Xaml;

namespace TemplateFlutter.UwpShell
{
    sealed partial class App : Application
    {
        public App() => InitializeComponent();

        protected override void OnLaunched(LaunchActivatedEventArgs e)
        {
            var f = Window.Current.Content as Frame;
            if (f == null)
            {
                f = new Frame();
                Window.Current.Content = f;
            }
            if (f.Content is null) f.Navigate(typeof(MainPage));
            Window.Current.Activate();
        }
    }
}
