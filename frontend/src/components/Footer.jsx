import React from 'react';
import { Camera, Video, Palette, Heart } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="bg-primary-900 text-white">
      <div className="container-max section-padding">
        <div className="grid md:grid-cols-4 gap-8">
          {/* Logo and Description */}
          <div className="md:col-span-2">
            <h3 className="text-2xl font-bold mb-4">Portfolio</h3>
            <p className="text-gray-300 mb-4">
              Creative professional specializing in photography, videography, and 3D design. 
              Passionate about visual storytelling and bringing ideas to life.
            </p>
            <div className="flex gap-4">
              <Camera className="w-5 h-5 text-primary-300" />
              <Video className="w-5 h-5 text-primary-300" />
              <Palette className="w-5 h-5 text-primary-300" />
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="text-lg font-semibold mb-4">Quick Links</h4>
            <ul className="space-y-2">
              <li><a href="#home" className="text-gray-300 hover:text-white transition-colors">Home</a></li>
              <li><a href="#about" className="text-gray-300 hover:text-white transition-colors">About</a></li>
              <li><a href="#projects" className="text-gray-300 hover:text-white transition-colors">Projects</a></li>
              <li><a href="#contact" className="text-gray-300 hover:text-white transition-colors">Contact</a></li>
            </ul>
          </div>

          {/* Services */}
          <div>
            <h4 className="text-lg font-semibold mb-4">Services</h4>
            <ul className="space-y-2">
              <li><span className="text-gray-300">Photography</span></li>
              <li><span className="text-gray-300">Videography</span></li>
              <li><span className="text-gray-300">3D Design</span></li>
              <li><span className="text-gray-300">Creative Direction</span></li>
            </ul>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="border-t border-primary-800 mt-8 pt-8 text-center">
          <p className="text-gray-300 flex items-center justify-center gap-2">
            Made with <Heart className="w-4 h-4 text-red-400" /> by Portfolio Team
          </p>
          <p className="text-gray-400 text-sm mt-2">
            © 2024 Portfolio. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;