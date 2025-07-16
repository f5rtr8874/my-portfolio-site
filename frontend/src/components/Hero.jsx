import React from 'react';
import { ArrowDown } from 'lucide-react';

const Hero = () => {
  return (
    <section 
      id="home" 
      className="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary-900 via-primary-800 to-primary-700 text-white relative overflow-hidden"
    >
      {/* Background Image */}
      <div 
        className="absolute inset-0 bg-cover bg-center bg-no-repeat opacity-20"
        style={{
          backgroundImage: `url('https://images.unsplash.com/photo-1522204538344-922f76ecc041?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzV8MHwxfHNlYXJjaHwzfHxjcmVhdGl2ZSUyMHBvcnRmb2xpb3xlbnwwfHx8Ymx1ZXwxNzUyNzAwNjM5fDA&ixlib=rb-4.1.0&q=85')`
        }}
      ></div>

      {/* Content */}
      <div className="container-max text-center z-10">
        <div className="max-w-4xl mx-auto">
          <h1 className="text-5xl md:text-7xl font-bold mb-6 animate-fade-in">
            Creative
            <span className="block text-primary-200">Portfolio</span>
          </h1>
          
          <p className="text-xl md:text-2xl mb-8 text-gray-300 max-w-2xl mx-auto animate-slide-up">
            Showcasing my passion for photography, videography, and 3D design
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center animate-slide-up">
            <a 
              href="#projects" 
              className="btn-primary text-lg px-8 py-4 inline-flex items-center gap-2"
            >
              View My Work
            </a>
            <a 
              href="#contact" 
              className="btn-secondary text-lg px-8 py-4 inline-flex items-center gap-2"
            >
              Get In Touch
            </a>
          </div>
        </div>
      </div>

      {/* Scroll Indicator */}
      <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
        <a href="#about" className="text-white/70 hover:text-white transition-colors">
          <ArrowDown size={24} />
        </a>
      </div>
    </section>
  );
};

export default Hero;