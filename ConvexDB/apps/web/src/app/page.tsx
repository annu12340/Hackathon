'use client';
import Link from 'next/link';
import 'bootstrap/dist/css/bootstrap.min.css';

export default function Home() {
  return (
    <main>
         {/*Header */}
      <header id="home" className="header-area pt-100">
         <div className="shape header-shape-one">
            <img src={'/images/shape-1.png'} alt="shape" />
         </div>

         <div className="shape header-shape-tow animation-one">
            <img src={'/images/shape-2.png'}alt="shape" />
         </div>

         <div className="shape header-shape-three animation-one">
            <img src={'/images/shape-3.png'} alt="shape" />
         </div>

         <div className="shape header-shape-fore">
            <img src={'/images/shape-4.png'} alt="shape" />
         </div>

         <div className="navigation-bar">
            <div className="container">
               <div className="row">
                  <div className="col-lg-12">
                     <nav className="navbar navbar-expand-lg">
                        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                           <span className="toggler-icon"></span>
                           <span className="toggler-icon"></span>
                           <span className="toggler-icon"></span>
                        </button>

                        <div className="collapse navbar-collapse" id="navbarSupportedContent">
                           <ul id="nav" className="navbar-nav ml-auto">
                              <li className="nav-item active">
                                 <a className="page-scroll" href="#home">Home</a>
                              </li>
                              <li className="nav-item">
                                 <a className="page-scroll" href="#about">About</a>
                              </li>
                              <li className="nav-item">
                                 <a className="page-scroll" href="#">Info</a>
                              </li>
                              <li className="nav-item">
                                 <a className="page-scroll" href="#">Message</a>
                              </li>
                              <li className="nav-item">
                                 <a className="page-scroll" href="#">Report</a>
                              </li>
                              <li className="nav-item">
                                 <a className="page-scroll" href="#">Donate</a>
                              </li>
                           </ul>
                             {/*navbar nav */}
                        </div>

                     </nav>
                       {/*navbar */}
                  </div>
               </div>
                 {/*row */}
            </div>
              {/*container */}
         </div>
           {/*navigation bar */}

         <div className="header-banner d-flex align-items-center">
            <div className="container">
               <div className="row">
                  <div className="col-xl-8 col-lg-9 col-sm-10">
                     <div className="banner-content">
                        <h4 className="sub-title wow">With you, always</h4>
                        <h1 className="banner-title"><span>Sentinel</span> app</h1>
                       
                        <br />
                        <Link
                      href='/encode'
                      className='ml-20  main-btn'
                    >
                      Login
                    </Link>
                     </div>
                  </div>
               </div>
                 {/*row */}
            </div>
              {/*container */}
              <div className="banner-image bg_cover" style={{backgroundImage: "url('https://img.freepik.com/free-vector/flat-illustration-iranian-women-with-leaves-flowers_23-2149826001.jpg?t=st=1709571296~exp=1709574896~hmac=a61e4a8d0be5218a70f4e89f5e91e87bbd4fcd5e7c5411a78484e12659f49498&w=740')"}}></div>

         </div>
           {/*header banner */}
      </header>

      {/*   About */}
      <section id="about" className="about-area ">
         <div className="container">
            <div className="row">
               <div className="col-lg-6">
                  <div className="about-image mt-50 clearfix">
                     <div className="single-image float-left">
                        <img src="https://img.freepik.com/free-vector/woman-cage-pro-civil-rights-concept_23-2148584349.jpg?t=st=1709571863~exp=1709575463~hmac=582c923f7eeefbc57027b10df686e34662aefca9763e1fde60632b9842056f9f&w=740" alt="About" />
                     </div>

                     <div data-aos="fade-right" className="about-btn">
                        <a className="main-btn" href="#"><span>27</span> Years Experience</a>
                     </div>
                     <div className="single-image image-tow float-right">
                        <img src="https://img.freepik.com/free-vector/floral-women-s-day-with-fist-girls-power_23-2148421050.jpg?t=st=1709571533~exp=1709575133~hmac=befa9728d331f8b03febb0bc3f475c270d16bf1784b990cc9906be0be9b6d93b&w=740" alt="About" />
                     </div>
                  </div>
                    {/*about image */}
               </div>
               <div className="col-lg-6">
                  <div className="about-content mt-45">
                     <h4 className="about-welcome">About Us</h4>
                     <h3 className="about-title mt-10">Reasons to choose</h3>
                     <p className="mt-25">
                     In times of crisis, speed and effectiveness can mean the difference between life and death. Unfortunately, existing emergency response systems often fail to address the unique needs of women in peril. Enter Sentinel: a beacon of hope and empowerment designed specifically for women facing danger.

Our shelter, aptly named Sentinel, goes beyond mere refuge—it's a tailored sanctuary for women in crisis. We recognize the urgency of gathering critical victim information swiftly, enabling covert communication for those in danger, and providing a secure haven from repeat offenders.

But Sentinel is more than just bricks and mortar. It's a cutting-edge platform that seamlessly integrates advanced technologies to deliver real-time support and resources. Our mission is to redefine how we protect and uplift women during moments of uncertainty.

<br />
                        <br />Join us in our quest to create a world where every woman feels safe, supported, and empowered to thrive. Together, we can make a difference and build a future where women's safety is non-negotiable.
                     </p>
                     <a className="main-btn mt-25" href="#">learn more</a>
                  </div>
                    {/*about content */}
               </div>
            </div>
              {/*row */}
         </div>
      </section>
      <br />
      <br />
      <br />
        {/*Map */}
      <section id="map" className="map-area">
         <div className="mapouter">
            <div className="gmap_canvas">
               <iframe id="gmap_canvas" src="https://maps.google.com/maps?q=university%20of%20san%20francisco&t=&z=13&ie=UTF8&iwloc=&output=embed" scrolling="no"></iframe>
            </div>
         </div>
         <div
            className="map-bg bg_cover d-none d-lg-block"
            style={{backgroundImage: "url('https://img.freepik.com/free-vector/colorful-women-s-day-pattern-with-women-faces_23-2148412959.jpg?t=st=1709571937~exp=1709575537~hmac=787c538125ea51a4e52b9882dd0078ed066986617a55f7a02f827a4edb6a11ac&w=740')"}}
         ></div>
      </section>

    </main>
  );
}
