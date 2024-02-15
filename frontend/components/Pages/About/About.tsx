import Image from 'next/image';
import Link from 'next/link';

import classes from './About.module.scss';

import comp1 from '../../../assets/images/sample-comp-1.png';
import comp2 from '../../../assets/images/sample-comp-2.png';
import comp3 from '../../../assets/images/sample-comp-3.png';
import logo from '../../../assets/images/logo.png';

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
        <div className={classes.aboutCard}>
          <h3>Zenith Tech 1.0</h3>
          <h1>I</h1>
          <p className='paragraph'>
            Where innovation meets excitement! At our store, we pride ourselves
            on offering the latest and greatest in gaming technology, gadgets,
            and gear. Step into a world where every click, tap, and swipe takes
            you on an adventure beyond imagination.
          </p>
        </div>
        <div className={classes.aboutCard}>
          <h3>Zenith Tech 1.0</h3>
          <h1>II</h1>
          <p className='paragraph'>
            Browse through our curated selection of cutting-edge gaming PCs,
            consoles, peripherals, and accessories, meticulously chosen to cater
            to every type of gamer. From high-performance rigs that can handle
            the most demanding titles to sleek and stylish accessories that add
            flair to your setup, we&apos;ve got it all.
          </p>
        </div>
        <div className={classes.aboutCard}>
          <h3>Zenith Tech 1.0</h3>
          <h1>III</h1>
          <p className='paragraph'>
            Join us for regular gaming tournaments, workshops, and events where
            you can connect with fellow gamers, learn new skills, and immerse
            yourself in the ever-evolving world of technology. Whether you&apos;re a
            seasoned pro or just starting your gaming journey, there&apos;s a place
            for you here at Zenith Tech.
          </p>
        </div>
      </section>
      <section className={classes.featureSub}>
        <figure>
          <Image src={comp2} alt='Zenith Tech Feature Composition' />
          <figcaption>
            <p className={classes.paragraph}>
              Explore a diverse range of categories effortlessly with our
              intuitive top navigation, designed to streamline your browsing
              experience and help you discover exactly what you&apos;re looking for.
            </p>
          </figcaption>
        </figure>
      </section>
      <section className={classes.featureSub}>
        <figure>
          <Image src={comp3} alt='Zenith Tech Feature Composition' />
          <figcaption>
            <p className={classes.paragraph}>
              Harness the power of our versatile search bar to explore a wide
              array of products tailored to your needs. Whether you&apos;re hunting
              for the gaming consoles, gift cards, or must-have tech
              accessories, our search feature puts the entire inventory at your
              fingertips.
            </p>
          </figcaption>
        </figure>
      </section>
      <footer className={classes.footer}>
        <div className={classes.logo}>
          <Link href='/'>
            <Image src={logo} alt='Zenith Tech' />
          </Link>
        </div>
        <p className={classes.paragraph}>
          Copyright &copy; 2024. Prosper Emebo.
        </p>
      </footer>
    </>
  );
}

export default About;
