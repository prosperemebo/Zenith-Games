import Image from 'next/image';
import classes from './About.module.scss';

import comp1 from '../../../assets/images/sample-comp-1.png';

function About() {
  return (
    <>
      <header className={classes.header}>
        <div className={classes.textbox}>
          <h3>ZENITH TECH 1.0</h3>
          <h1 className={classes.headingPrimary}>
            Sounds <br />
            Like An <br /> Upgrade
          </h1>
          <p className={classes.paragraph}>No 1 stop for tech enthusiasts.</p>
        </div>
      </header>
      <section className={classes.featureMain}>
        <figure>
          <Image src={comp1} alt='Zenith Tech Feature Composition' />
        </figure>
      </section>
      <section className={classes.about}>
        
      </section>
    </>
  );
}

export default About;
