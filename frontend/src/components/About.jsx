import React from 'react';
import { Camera, Video, Palette } from 'lucide-react';

const About = () => {
  const skills = [
    {
      icon: <Camera className="w-8 h-8" />,
      title: "Photography",
      description: "Capturing moments and telling stories through the lens. Specializing in portrait, landscape, and commercial photography."
    },
    {
      icon: <Video className="w-8 h-8" />,
      title: "Videography",
      description: "Creating compelling visual narratives through motion. From corporate videos to creative storytelling."
    },
    {
      icon: <Palette className="w-8 h-8" />,
      title: "3D Design",
      description: "Bringing ideas to life through three-dimensional design. From concept to final render."
    }
  ];

  return (
    <section id="about" className="section-padding bg-gray-50">
      <div className="container-max">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-primary-900 mb-6">
            About Me
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            I'm a passionate visual storyteller with a love for creating compelling content 
            across multiple mediums. My work spans photography, videography, and 3D design, 
            always striving to capture the essence of each project.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8 mb-16">
          {skills.map((skill, index) => (
            <div key={index} className="text-center p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow">
              <div className="text-primary-600 mb-4 flex justify-center">
                {skill.icon}
              </div>
              <h3 className="text-xl font-semibold text-primary-900 mb-3">
                {skill.title}
              </h3>
              <p className="text-gray-600">
                {skill.description}
              </p>
            </div>
          ))}
        </div>

        <div className="bg-white rounded-lg shadow-md p-8 md:p-12">
          <div className="grid md:grid-cols-2 gap-8 items-center">
            <div>
              <h3 className="text-2xl font-bold text-primary-900 mb-4">
                My Journey
              </h3>
              <p className="text-gray-600 mb-4">
                With over 5 years of experience in the creative industry, I've had the privilege 
                of working with diverse clients and projects. My passion for visual storytelling 
                drives me to continuously push creative boundaries.
              </p>
              <p className="text-gray-600 mb-6">
                Whether it's capturing the perfect moment through photography, creating engaging 
                video content, or designing stunning 3D visualizations, I approach each project 
                with dedication and creativity.
              </p>
              <div className="flex flex-wrap gap-2">
                {['Photography', 'Videography', '3D Design', 'Creative Direction', 'Post-Production'].map((skill, index) => (
                  <span key={index} className="bg-primary-100 text-primary-800 px-3 py-1 rounded-full text-sm">
                    {skill}
                  </span>
                ))}
              </div>
            </div>
            <div className="text-center">
              <div className="w-48 h-48 bg-primary-200 rounded-full mx-auto mb-4 flex items-center justify-center">
                <span className="text-primary-600 text-6xl font-bold">
                  JD
                </span>
              </div>
              <p className="text-gray-600">
                Ready to bring your vision to life
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;